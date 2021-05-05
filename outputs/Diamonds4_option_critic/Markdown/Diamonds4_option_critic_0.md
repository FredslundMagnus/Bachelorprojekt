
# Parameters

    Name :                      Diamonds4_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal7
    Failed actions chance :     0.0
    Hours :                     72.0
    Batch :                     25
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      52040312087 function calls (50352068292 primitive calls) in 258900.45 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.455 258900.455 {built-in method builtins.exec}
                      1    0.365    0.365 258900.455 258900.455 <string>:1(<module>)
                      1 6221.487 6221.487 258900.090 258900.090 optionCritic.py:195(option_critic_run)
               60037100 9488.685    0.000 112471.369    0.002 optionCritic.py:143(actor_loss_fn)
        2229505263/549066825 10131.537    0.000 111633.129    0.000 module.py:866(_call_impl)
              186715382  830.596    0.000 103973.939    0.001 optionCritic.py:70(get_state)
              186715382 2317.966    0.000 100565.590    0.001 container.py:117(forward)
                2401484   18.193    0.000 74263.260    0.031 tensor.py:195(backward)
                2401484   24.674    0.000 74244.752    0.031 __init__.py:68(backward)
                2401484 74157.688    0.031 74157.688    0.031 {method 'run_backward' of 'torch._C._EngineBase' objects}
              373430764 1011.217    0.000 63104.538    0.000 conv.py:398(forward)
              373430764  533.645    0.000 61694.371    0.000 conv.py:390(_conv_forward)
              373430764 61160.726    0.000 61160.726    0.000 {built-in method conv2d}
               60037100 3661.274    0.000 21514.650    0.000 optionCritic.py:91(get_action)
              735782207 1611.729    0.000 21388.704    0.000 linear.py:93(forward)
              735782207  630.181    0.000 19065.927    0.000 functional.py:1737(linear)
              735782207 18285.285    0.000 18285.285    0.000 {built-in method torch._C._nn.linear}
               60037100 1270.898    0.000 14718.741    0.000 optionCritic.py:80(predict_option_termination)
              120074200 1313.153    0.000 8321.531    0.000 distribution.py:34(__init__)
              560146146  523.660    0.000 7488.350    0.000 activation.py:713(forward)
                2401484   59.466    0.000 7339.640    0.003 optimizer.py:84(wrapper)
               60037100  636.427    0.000 7151.688    0.000 categorical.py:115(log_prob)
                2401484   30.202    0.000 7131.080    0.003 grad_mode.py:24(decorate_context)
                2401484  139.576    0.000 7047.037    0.003 rmsprop.py:56(step)
              560146146  531.624    0.000 6964.690    0.000 functional.py:1364(leaky_relu)
                2401484  138.473    0.000 6752.978    0.003 _functional.py:203(rmsprop)
              560146146 6324.656    0.000 6324.656    0.000 {built-in method torch._C._nn.leaky_relu}
               60037100  815.881    0.000 6044.087    0.000 categorical.py:49(__init__)
               60037100  505.049    0.000 5796.145    0.000 bernoulli.py:34(__init__)
              181639772  381.072    0.000 5663.012    0.000 optionCritic.py:77(get_Q)
                 600371   98.985    0.000 4833.701    0.008 optionCritic.py:116(critic_loss_fn)
              120674571  401.740    0.000 4386.823    0.000 optionCritic.py:88(get_terminations)
               60037100 2482.457    0.000 3666.492    0.000 constraints.py:398(check)
                2401484   12.178    0.000 3582.259    0.001 game.py:41(step)
                2401484   21.728    0.000 3441.113    0.001 layers.py:718(step)
               33620770 3068.078    0.000 3068.078    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               60037100  500.480    0.000 2875.331    0.000 distribution.py:240(_validate_sample)
               33620770 2189.218    0.000 2189.218    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               60037100  450.524    0.000 2182.670    0.000 bernoulli.py:86(sample)
              186715382  236.954    0.000 2131.099    0.000 activation.py:101(forward)
                2401484   94.667    0.000 2106.425    0.001 layers.py:17(step)
               60037100 2104.414    0.000 2104.414    0.000 constraints.py:364(check)
               60037100  154.750    0.000 2003.576    0.000 layer.py:98(move)
               60037100 1026.429    0.000 1977.090    0.000 categorical.py:123(entropy)
              186715382  234.184    0.000 1894.145    0.000 functional.py:1195(relu)
             2887879222 1876.183    0.000 1876.367    0.000 module.py:934(__getattr__)
               60037100 1858.479    0.000 1858.479    0.000 constraints.py:249(check)
              180111300  241.989    0.000 1774.264    0.000 utils.py:106(__get__)
              420259700 1741.506    0.000 1741.506    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              186715382  167.656    0.000 1643.660    0.000 flatten.py:39(forward)
              186715382 1632.072    0.000 1632.072    0.000 {built-in method relu}
              181312042  203.507    0.000 1585.874    0.000 tensor.py:525(__rsub__)
              120074200  533.793    0.000 1569.157    0.000 functional.py:46(broadcast_tensors)
                 600371 1279.610    0.002 1525.912    0.003 replaybuffer.py:42(sample_option_critic)
               26416324   61.548    0.000 1490.280    0.000 tensor.py:575(__iter__)
              186715382 1476.003    0.000 1476.003    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               60037100  391.081    0.000 1401.169    0.000 categorical.py:108(sample)
               26416324 1392.467    0.000 1392.467    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              181312042 1351.971    0.000 1351.971    0.000 {built-in method rsub}
               60037100   73.401    0.000 1346.656    0.000 categorical.py:88(logits)
               60037100  299.396    0.000 1323.705    0.000 utils.py:11(broadcast_all)
                2401485  199.156    0.000 1304.203    0.001 layers.py:684(update)
              120674571 1284.532    0.000 1284.532    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               60037100   74.271    0.000 1273.255    0.000 utils.py:82(probs_to_logits)
              180711671 1256.845    0.000 1256.845    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              180111300 1242.661    0.000 1242.661    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             2255921587 1221.414    0.000 1221.414    0.000 {built-in method torch._C._get_tracing_state}
             9642254226 1150.615    0.000 1168.154    0.000 {built-in method builtins.len}
               60037100  249.161    0.000 1158.084    0.000 layers.py:735(check)
              180111300 1024.497    0.000 1024.497    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             9104736434  950.339    0.000  950.339    0.000 {method 'values' of 'collections.OrderedDict' objects}
               60037100  926.500    0.000  926.500    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              120074200  872.609    0.000  872.609    0.000 {built-in method broadcast_tensors}
                2401484   93.668    0.000  796.388    0.000 replaybuffer.py:34(save_option_critic)
                2401484  108.435    0.000  765.335    0.000 optimizer.py:189(zero_grad)
               60037100  155.441    0.000  751.835    0.000 utils.py:77(clamp_probs)
              181912413  657.142    0.000  657.142    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               60037100  648.973    0.000  648.973    0.000 {built-in method bernoulli}
               60037100  603.699    0.000  603.699    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               60037100  596.394    0.000  596.394    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               60364830  590.008    0.000  590.008    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               33620770  564.225    0.000  564.225    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               60037100  116.074    0.000  555.375    0.000 layers.py:729(isFree)
               12458080  256.525    0.000  550.678    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              361423342  526.950    0.000  526.950    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              120074200  517.255    0.000  517.255    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               33620770  511.038    0.000  511.038    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               60037100  508.905    0.000  508.905    0.000 {built-in method clamp}
               16810395  283.545    0.000  470.408    0.000 layer.py:167(NoRock_update)
              792862955  321.520    0.000  469.858    0.000 {built-in method builtins.isinstance}
               16210021  453.478    0.000  453.478    0.000 {built-in method tensor}
               60037100  447.148    0.000  447.148    0.000 {built-in method log}
              180443856  440.455    0.000  440.455    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              407695265  366.248    0.000  439.302    0.000 layer.py:95(isFree)
               60037100  431.055    0.000  431.055    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              186715396  397.773    0.000  397.773    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               60037100  396.769    0.000  396.769    0.000 {built-in method all}
               33620756  385.658    0.000  385.658    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               60037100  358.466    0.000  358.466    0.000 {built-in method multinomial}
                7204456   14.327    0.000  347.378    0.000 game.py:37(board)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601866: <Diamonds4_option_critic_0> in cluster <dcc> Done

Job <Diamonds4_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:11 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:13 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:13 2021
Terminated at Sun May  2 21:36:16 2021
Results reported at Sun May  2 21:36:16 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258285.88 sec.
    Max Memory :                                 869 MB
    Average Memory :                             857.78 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15515.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258918 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.



# Parameters

    Name :                      Lights1_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal3
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


      58014938278 function calls (56157906614 primitive calls) in 258900.58 seconds

##    Ordered by: cumulative time
   List reduced from 433 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.582 258900.582 {built-in method builtins.exec}
                      1    0.277    0.277 258900.582 258900.582 <string>:1(<module>)
                      1 5778.739 5778.739 258900.305 258900.305 optionCritic.py:195(option_critic_run)
               66039525 9454.805    0.000 114410.906    0.002 optionCritic.py:143(actor_loss_fn)
        2452822115/604375808 10405.033    0.000 113269.785    0.000 module.py:866(_call_impl)
              205382923  862.091    0.000 105476.727    0.001 optionCritic.py:70(get_state)
              205382923 2435.030    0.000 101966.702    0.000 container.py:117(forward)
                2641581   18.704    0.000 73847.582    0.028 tensor.py:195(backward)
                2641581   24.339    0.000 73828.524    0.028 __init__.py:68(backward)
                2641581 73748.051    0.028 73748.051    0.028 {method 'run_backward' of 'torch._C._EngineBase' objects}
              410765846  978.946    0.000 64767.549    0.000 conv.py:398(forward)
              410765846  560.625    0.000 63370.764    0.000 conv.py:390(_conv_forward)
              410765846 62810.139    0.000 62810.139    0.000 {built-in method conv2d}
               66039525 3914.556    0.000 22860.557    0.000 optionCritic.py:91(get_action)
              809758731 1698.658    0.000 20562.943    0.000 linear.py:93(forward)
              809758731  674.423    0.000 18138.376    0.000 functional.py:1737(linear)
              809758731 17308.858    0.000 17308.858    0.000 {built-in method torch._C._nn.linear}
               66039525 1237.477    0.000 13899.104    0.000 optionCritic.py:80(predict_option_termination)
              132079050 1281.961    0.000 8345.984    0.000 distribution.py:34(__init__)
               66039525  671.706    0.000 7623.537    0.000 categorical.py:115(log_prob)
              616148769  553.093    0.000 7550.365    0.000 activation.py:713(forward)
              616148769  576.815    0.000 6997.271    0.000 functional.py:1364(leaky_relu)
               66039525  862.596    0.000 6387.411    0.000 categorical.py:49(__init__)
              616148769 6307.223    0.000 6307.223    0.000 {built-in method torch._C._nn.leaky_relu}
              200213915  419.529    0.000 5785.472    0.000 optionCritic.py:77(get_Q)
                2641581   55.224    0.000 5519.496    0.002 optimizer.py:84(wrapper)
                2641581   26.678    0.000 5323.786    0.002 grad_mode.py:24(decorate_context)
               66039525  410.561    0.000 5265.677    0.000 bernoulli.py:34(__init__)
                2641581  140.317    0.000 5248.076    0.002 rmsprop.py:56(step)
                2641581  141.111    0.000 4947.321    0.002 _functional.py:203(rmsprop)
                 660395   91.783    0.000 4787.831    0.007 optionCritic.py:116(critic_loss_fn)
              132739445  417.828    0.000 4514.857    0.000 optionCritic.py:88(get_terminations)
                2641581   12.733    0.000 4235.700    0.002 game.py:41(step)
                2641581   22.733    0.000 4089.512    0.002 layers.py:718(step)
               66039525 2597.668    0.000 3862.304    0.000 constraints.py:398(check)
               66039525  538.192    0.000 3055.050    0.000 distribution.py:240(_validate_sample)
                2641581   91.465    0.000 2517.564    0.001 layers.py:17(step)
               66039525  156.228    0.000 2417.078    0.000 layer.py:98(move)
              205382923  239.895    0.000 2153.840    0.000 activation.py:101(forward)
               36982128 2103.891    0.000 2103.891    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               66039525 1091.333    0.000 2097.548    0.000 categorical.py:123(entropy)
               66039525 2020.486    0.000 2020.486    0.000 constraints.py:364(check)
               66039525 1967.016    0.000 1967.016    0.000 constraints.py:249(check)
             3177847467 1934.543    0.000 1934.723    0.000 module.py:934(__getattr__)
               66039525  368.423    0.000 1934.012    0.000 bernoulli.py:86(sample)
              205382923  207.536    0.000 1913.945    0.000 functional.py:1195(relu)
              198118575  263.891    0.000 1905.813    0.000 utils.py:106(__get__)
              462276675 1802.908    0.000 1802.908    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              205382923  202.067    0.000 1718.709    0.000 flatten.py:39(forward)
              205382923 1676.195    0.000 1676.195    0.000 {built-in method relu}
              199439365  229.075    0.000 1628.162    0.000 tensor.py:525(__rsub__)
              132079050  555.154    0.000 1571.532    0.000 functional.py:46(broadcast_tensors)
                2641582  191.843    0.000 1539.983    0.001 layers.py:684(update)
              205382923 1516.642    0.000 1516.642    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               66039525  425.652    0.000 1509.657    0.000 categorical.py:108(sample)
               36982128 1489.196    0.000 1489.196    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               66039525   74.187    0.000 1426.866    0.000 categorical.py:88(logits)
               29057391   64.783    0.000 1400.297    0.000 tensor.py:575(__iter__)
               66039525  310.267    0.000 1384.919    0.000 layers.py:735(check)
              199439365 1368.473    0.000 1368.473    0.000 {built-in method rsub}
               66039525   81.752    0.000 1352.679    0.000 utils.py:82(probs_to_logits)
             2481879506 1329.116    0.000 1329.116    0.000 {built-in method torch._C._get_tracing_state}
              198118575 1316.363    0.000 1316.363    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 660395 1066.294    0.002 1303.635    0.002 replaybuffer.py:42(sample_option_critic)
               29057391 1296.630    0.000 1296.630    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              198778970 1286.328    0.000 1286.328    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              132739445 1270.848    0.000 1270.848    0.000 {method 'max' of 'torch._C._TensorBase' objects}
            10672027744 1228.931    0.000 1246.706    0.000 {built-in method builtins.len}
               66039525  238.120    0.000 1179.391    0.000 utils.py:11(broadcast_all)
              198118575 1037.163    0.000 1037.163    0.000 {method 'all' of 'torch._C._TensorBase' objects}
            10016671383 1010.153    0.000 1010.153    0.000 {method 'values' of 'collections.OrderedDict' objects}
               66039525  949.815    0.000  949.815    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              132079050  855.825    0.000  855.825    0.000 {built-in method broadcast_tensors}
               66039525  176.690    0.000  801.789    0.000 utils.py:77(clamp_probs)
                2641581   90.274    0.000  787.992    0.000 replaybuffer.py:34(save_option_critic)
               66039525  132.267    0.000  738.900    0.000 layers.py:729(isFree)
               14530491  321.960    0.000  677.597    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                2641581  111.618    0.000  675.023    0.000 optimizer.py:189(zero_grad)
              200099760  667.045    0.000  667.045    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               66039525  636.764    0.000  636.764    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               66039525  625.099    0.000  625.099    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               66039525  618.042    0.000  618.042    0.000 {built-in method bernoulli}
              474150152  504.290    0.000  606.633    0.000 layer.py:95(isFree)
               66814075  571.418    0.000  571.418    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              132079050  555.892    0.000  555.892    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
              397557940  551.797    0.000  551.797    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               21132656  316.956    0.000  536.388    0.000 layer.py:167(NoRock_update)
               66039525  531.863    0.000  531.863    0.000 {built-in method clamp}
               36982128  480.042    0.000  480.042    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               66039525  469.138    0.000  469.138    0.000 {built-in method log}
               66039525  453.819    0.000  453.819    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               36982128  450.983    0.000  450.983    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               17830675  441.144    0.000  441.144    0.000 {built-in method tensor}
               66039525  437.232    0.000  437.232    0.000 {built-in method all}
              205382937  410.274    0.000  410.274    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              875230471  261.228    0.000  387.886    0.000 {built-in method builtins.isinstance}
               66039525  384.533    0.000  384.533    0.000 {built-in method multinomial}
              198898431  362.763    0.000  362.763    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               14530491   21.468    0.000  355.637    0.000 <__array_function__ internals>:2(prod)
                7924747   14.603    0.000  331.068    0.000 game.py:37(board)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601853: <Lights1_option_critic_2> in cluster <dcc> Done

Job <Lights1_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:02 2021
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:05 2021
Terminated at Sun May  2 21:36:11 2021
Results reported at Sun May  2 21:36:11 2021

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

    CPU time :                                   258290.00 sec.
    Max Memory :                                 909 MB
    Average Memory :                             896.36 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15475.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258918 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.


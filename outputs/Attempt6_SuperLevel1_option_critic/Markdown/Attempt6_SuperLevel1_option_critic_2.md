
# Parameters

    Name :                      Attempt6_SuperLevel1_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     32
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      37175303187 function calls (36127746240 primitive calls) in 258900.77 seconds

##    Ordered by: cumulative time
   List reduced from 444 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.772 258900.772 {built-in method builtins.exec}
                      1    0.358    0.358 258900.772 258900.772 <string>:1(<module>)
                      1 3987.881 3987.881 258900.415 258900.415 optionCritic.py:195(option_critic_run)
                1174391    9.422    0.000 132232.747    0.113 tensor.py:195(backward)
                1174391   12.517    0.000 132223.152    0.113 __init__.py:68(backward)
                1174391 132184.384    0.113 132184.384    0.113 {method 'run_backward' of 'torch._C._EngineBase' objects}
        1387918996/344179006 6610.118    0.000 78031.264    0.000 module.py:866(_call_impl)
               37580512 5661.354    0.000 77326.401    0.002 optionCritic.py:143(actor_loss_fn)
              115971110  574.234    0.000 72917.726    0.001 optionCritic.py:70(get_state)
              115971110 1520.425    0.000 70719.946    0.001 container.py:117(forward)
              231942220  647.219    0.000 44508.001    0.000 conv.py:398(forward)
              231942220  340.510    0.000 43605.032    0.000 conv.py:390(_conv_forward)
              231942220 43264.522    0.000 43264.522    0.000 {built-in method conv2d}
              460150116 1105.005    0.000 15669.372    0.000 linear.py:93(forward)
              460150116  432.941    0.000 14106.454    0.000 functional.py:1737(linear)
              460150116 13568.638    0.000 13568.638    0.000 {built-in method torch._C._nn.linear}
               37580512 2224.138    0.000 13226.885    0.000 optionCritic.py:91(get_action)
               37580512  795.917    0.000 9340.812    0.000 optionCritic.py:80(predict_option_termination)
                1174391   26.639    0.000 5826.305    0.005 optimizer.py:84(wrapper)
                1174391   15.522    0.000 5723.425    0.005 grad_mode.py:24(decorate_context)
                1174391   72.976    0.000 5679.018    0.005 adam.py:55(step)
                1174391  451.976    0.000 5527.481    0.005 _functional.py:53(adam)
               75161024  827.511    0.000 5249.840    0.000 distribution.py:34(__init__)
              347913330  364.686    0.000 4911.408    0.000 activation.py:713(forward)
                1174391    7.381    0.000 4655.862    0.004 game.py:42(step)
                1174391   11.134    0.000 4553.362    0.004 layers.py:827(step)
              347913330  374.720    0.000 4546.722    0.000 functional.py:1364(leaky_relu)
               37580512  363.201    0.000 4385.323    0.000 categorical.py:115(log_prob)
              347913330 4096.168    0.000 4096.168    0.000 {built-in method torch._C._nn.leaky_relu}
              115172763  261.920    0.000 3781.411    0.000 optionCritic.py:77(get_Q)
               37580512  502.236    0.000 3730.118    0.000 categorical.py:49(__init__)
               37580512  297.857    0.000 3723.851    0.000 bernoulli.py:34(__init__)
                 293597   50.967    0.000 3143.286    0.011 optionCritic.py:116(critic_loss_fn)
               75454621  268.817    0.000 2929.390    0.000 optionCritic.py:88(get_terminations)
                1174391   56.861    0.000 2849.688    0.002 layers.py:17(step)
               37580512  152.490    0.000 2787.898    0.000 layer.py:106(move)
               37580512 1535.380    0.000 2276.977    0.000 constraints.py:398(check)
               37580512  340.641    0.000 1970.812    0.000 layers.py:844(check)
               37580512  319.419    0.000 1790.845    0.000 distribution.py:240(_validate_sample)
                1174392  113.720    0.000 1687.024    0.001 layers.py:793(update)
              115971110  194.901    0.000 1428.707    0.000 activation.py:101(forward)
               37580512 1389.637    0.000 1389.637    0.000 constraints.py:364(check)
               37580512  273.971    0.000 1371.587    0.000 bernoulli.py:86(sample)
              115971110  139.102    0.000 1233.805    0.000 functional.py:1195(relu)
               37580512  634.752    0.000 1226.811    0.000 categorical.py:123(entropy)
               32882936 1197.992    0.000 1197.992    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1803677421 1193.843    0.000 1193.930    0.000 module.py:934(__getattr__)
               37580512 1160.878    0.000 1160.878    0.000 constraints.py:249(check)
              112741536  148.697    0.000 1090.280    0.000 utils.py:106(__get__)
              115971110  117.838    0.000 1075.141    0.000 flatten.py:39(forward)
              115971110 1073.420    0.000 1073.420    0.000 {built-in method relu}
              113328730  124.057    0.000 1058.702    0.000 tensor.py:525(__rsub__)
              263063584 1056.808    0.000 1056.808    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               16441468  984.808    0.000  984.808    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               16441468  976.829    0.000  976.829    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               75161024  343.990    0.000  958.284    0.000 functional.py:46(broadcast_tensors)
              115971110  957.303    0.000  957.303    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              113328730  914.349    0.000  914.349    0.000 {built-in method rsub}
               75454621  860.277    0.000  860.277    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               37580512  234.326    0.000  854.855    0.000 categorical.py:108(sample)
               12918301   33.497    0.000  842.911    0.000 tensor.py:575(__iter__)
               37580512   43.122    0.000  828.386    0.000 categorical.py:88(logits)
               37580512  184.860    0.000  827.124    0.000 utils.py:11(broadcast_all)
              113035133  823.734    0.000  823.734    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             1400837297  822.877    0.000  822.877    0.000 {built-in method torch._C._get_tracing_state}
               12918301  790.131    0.000  790.131    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               37580512   46.056    0.000  785.265    0.000 utils.py:82(probs_to_logits)
              112741536  780.472    0.000  780.472    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             6189441526  761.967    0.000  771.170    0.000 {built-in method builtins.len}
                 293597  538.131    0.002  666.788    0.002 replaybuffer.py:42(sample_option_critic)
             5667647094  659.357    0.000  659.357    0.000 {method 'values' of 'collections.OrderedDict' objects}
              112741536  652.205    0.000  652.205    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               16441468  647.626    0.000  647.626    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               32882936  634.467    0.000  634.467    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               16441468  627.154    0.000  627.154    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               37580512  135.967    0.000  592.848    0.000 layers.py:838(isFree)
               37580512  591.599    0.000  591.599    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               15267096  370.567    0.000  575.951    0.000 layer.py:159(update)
               75161024  513.650    0.000  513.650    0.000 {built-in method broadcast_tensors}
                1174391   55.257    0.000  494.005    0.000 replaybuffer.py:34(save_option_critic)
               37580512   96.539    0.000  466.569    0.000 utils.py:77(clamp_probs)
              442035429  357.768    0.000  456.881    0.000 layer.py:103(isFree)
                1844066   33.436    0.000  446.154    0.000 layers.py:849(restart)
               37580512  318.414    0.000  439.268    0.000 layers.py:471(check)
              113622327  421.136    0.000  421.136    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               37580512  412.807    0.000  412.807    0.000 {built-in method bernoulli}
             1287458015  283.087    0.000  402.454    0.000 enum.py:646(__hash__)
               37580512  375.620    0.000  375.620    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               39424545  374.150    0.000  374.150    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              112741568   98.666    0.000  373.574    0.000 {built-in method builtins.all}
               37580512  370.031    0.000  370.031    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1174391   55.692    0.000  356.830    0.000 optimizer.py:189(zero_grad)
              226070266  350.840    0.000  350.840    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               75161024  321.802    0.000  321.802    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               37580512  313.034    0.000  313.034    0.000 {built-in method clamp}
               37580512  227.603    0.000  307.052    0.000 layers.py:77(check)
              494602013  185.809    0.000  301.706    0.000 {built-in method builtins.isinstance}
                4724542  138.777    0.000  291.462    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7927141  286.684    0.000  286.684    0.000 {built-in method tensor}
               37580512  272.640    0.000  272.640    0.000 {built-in method log}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624161: <Attempt6_SuperLevel1_option_critic_2> in cluster <dcc> Done

Job <Attempt6_SuperLevel1_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
Job was executed on host(s) <n-62-11-63>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:28 2021
Terminated at Wed May 12 01:17:35 2021
Results reported at Wed May 12 01:17:35 2021

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

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258287.98 sec.
    Max Memory :                                 1310 MB
    Average Memory :                             1292.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15074.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258957 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.


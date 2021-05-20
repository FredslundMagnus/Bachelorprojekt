[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt8_DoorsAndKey_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal1
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


      31081723141 function calls (30092444555 primitive calls) in 258901.27 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.267 258901.267 {built-in method builtins.exec}
                      1    0.578    0.578 258901.267 258901.267 <string>:1(<module>)
                      1 4706.119 4706.119 258900.689 258900.689 optionCritic.py:195(option_critic_run)
               35489792 9118.248    0.000 112193.293    0.003 optionCritic.py:143(actor_loss_fn)
        1310380393/324706864 10023.517    0.000 111315.061    0.000 module.py:866(_call_impl)
              109519281  902.475    0.000 102989.275    0.001 optionCritic.py:70(get_state)
              109519281 2725.606    0.000 99473.401    0.001 container.py:117(forward)
                1109056   12.649    0.000 69404.095    0.063 tensor.py:195(backward)
                1109056   13.316    0.000 69391.242    0.063 __init__.py:68(backward)
                1109056 69342.304    0.063 69342.304    0.063 {method 'run_backward' of 'torch._C._EngineBase' objects}
              219038562  933.339    0.000 60476.543    0.000 conv.py:398(forward)
              219038562  469.847    0.000 59179.314    0.000 conv.py:390(_conv_forward)
              219038562 58709.467    0.000 58709.467    0.000 {built-in method conv2d}
               35489792 4309.058    0.000 24976.007    0.001 optionCritic.py:91(get_action)
              434226145 1556.126    0.000 22529.535    0.000 linear.py:93(forward)
              434226145  591.933    0.000 20336.761    0.000 functional.py:1737(linear)
              434226145 19625.662    0.000 19625.662    0.000 {built-in method torch._C._nn.linear}
               35489792 1277.936    0.000 14230.760    0.000 optionCritic.py:80(predict_option_termination)
                1109056   32.858    0.000 13011.363    0.012 optimizer.py:84(wrapper)
                1109056   16.720    0.000 12877.542    0.012 grad_mode.py:24(decorate_context)
                1109056   78.580    0.000 12829.431    0.012 rmsprop.py:56(step)
                1109056  162.397    0.000 12667.840    0.011 _functional.py:203(rmsprop)
               15526778 10529.245    0.001 10529.245    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               70979584 1238.380    0.000 9005.678    0.000 distribution.py:34(__init__)
               35489792  723.990    0.000 8293.725    0.000 categorical.py:115(log_prob)
              328557843  451.853    0.000 7829.173    0.000 activation.py:713(forward)
              328557843  432.453    0.000 7377.320    0.000 functional.py:1364(leaky_relu)
               35489792  898.816    0.000 6967.873    0.000 categorical.py:49(__init__)
              328557843 6853.863    0.000 6853.863    0.000 {built-in method torch._C._nn.leaky_relu}
              108440943  492.762    0.000 6198.925    0.000 optionCritic.py:77(get_Q)
               35489792  364.654    0.000 5393.093    0.000 bernoulli.py:34(__init__)
               71256848  460.567    0.000 4939.905    0.000 optionCritic.py:88(get_terminations)
                 277264   71.152    0.000 4564.571    0.016 optionCritic.py:116(critic_loss_fn)
               35489792 2895.695    0.000 4332.615    0.000 constraints.py:398(check)
               35489792  531.643    0.000 3246.112    0.000 distribution.py:240(_validate_sample)
                1109056    8.323    0.000 2674.327    0.002 game.py:42(step)
                1109056   13.521    0.000 2532.021    0.002 layers.py:827(step)
              109519281  214.131    0.000 2476.494    0.000 activation.py:101(forward)
               35489792 1193.596    0.000 2325.016    0.000 categorical.py:123(entropy)
              109519281  178.917    0.000 2262.362    0.000 functional.py:1195(relu)
               35489792 2230.010    0.000 2230.010    0.000 constraints.py:364(check)
               35489792 2161.222    0.000 2161.222    0.000 constraints.py:249(check)
              106469376  271.056    0.000 2105.666    0.000 utils.py:106(__get__)
              109519281 2056.816    0.000 2056.816    0.000 {built-in method relu}
               35489792  363.582    0.000 2032.214    0.000 bernoulli.py:86(sample)
              248428544 2005.702    0.000 2005.702    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              109519281  161.260    0.000 1814.740    0.000 flatten.py:39(forward)
              107023904  189.955    0.000 1702.669    0.000 tensor.py:525(__rsub__)
             1702360105 1695.732    0.000 1695.845    0.000 module.py:934(__getattr__)
              109519281 1653.480    0.000 1653.480    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             1322580009 1652.866    0.000 1652.866    0.000 {built-in method torch._C._get_tracing_state}
               70979584  517.753    0.000 1645.254    0.000 functional.py:46(broadcast_tensors)
               35489792   77.371    0.000 1639.419    0.000 categorical.py:88(logits)
               35489792  440.064    0.000 1611.939    0.000 categorical.py:108(sample)
                1109057  144.422    0.000 1579.244    0.001 layers.py:793(update)
               35489792   93.019    0.000 1562.048    0.000 utils.py:82(probs_to_logits)
              106469376 1497.106    0.000 1497.106    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              107023904 1482.602    0.000 1482.602    0.000 {built-in method rsub}
              106746640 1453.653    0.000 1453.653    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               71256848 1341.108    0.000 1341.108    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               12199616   45.457    0.000 1246.262    0.000 tensor.py:575(__iter__)
               12199616 1162.445    0.000 1162.445    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              106469376 1157.747    0.000 1157.747    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               35489792  222.955    0.000 1150.066    0.000 utils.py:11(broadcast_all)
               35489792 1057.713    0.000 1057.713    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               70979584 1003.728    0.000 1003.728    0.000 {built-in method broadcast_tensors}
               15526778  942.206    0.000  942.206    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             5628332871  921.465    0.000  933.934    0.000 {built-in method builtins.len}
                1109056   56.334    0.000  932.654    0.001 layers.py:17(step)
               35489792  176.834    0.000  931.886    0.000 utils.py:77(clamp_probs)
               35489792   93.406    0.000  872.163    0.000 layer.py:106(move)
                1417073   31.017    0.000  837.578    0.001 layers.py:849(restart)
             5351040853  777.154    0.000  777.154    0.000 {method 'values' of 'collections.OrderedDict' objects}
              107301168  761.841    0.000  761.841    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               35489792  755.052    0.000  755.052    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               15291679  353.667    0.000  752.642    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               35489792  736.894    0.000  736.894    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               35489792  720.021    0.000  720.021    0.000 {built-in method bernoulli}
                1109056   75.322    0.000  714.798    0.001 replaybuffer.py:34(save_option_critic)
               36906831  668.196    0.000  668.196    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1417073   14.346    0.000  648.600    0.000 level.py:8(__init__)
                 277264  499.764    0.002  639.468    0.002 replaybuffer.py:42(sample_option_critic)
              213493280  627.047    0.000  627.047    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               35489792  624.634    0.000  624.634    0.000 {built-in method clamp}
               70979584  622.853    0.000  622.853    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1417073   28.279    0.000  544.411    0.000 levels.py:122(generate)
               35489792  537.143    0.000  537.143    0.000 {built-in method log}
               35489792  501.909    0.000  501.909    0.000 {built-in method all}
                5526778   80.500    0.000  491.584    0.000 level.py:41(notUsed)
               35489792  487.552    0.000  487.552    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              109519295  481.350    0.000  481.350    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               35489792  139.640    0.000  462.418    0.000 layers.py:844(check)
               15526778  437.166    0.000  437.166    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               35489792  417.519    0.000  417.519    0.000 {built-in method multinomial}
               15291679   24.013    0.000  398.975    0.000 <__array_function__ internals>:2(prod)
              467085479  230.915    0.000  374.240    0.000 {built-in method builtins.isinstance}
                1109056   68.807    0.000  370.973    0.000 optimizer.py:189(zero_grad)
               15291679   21.871    0.000  370.215    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               15291679   35.085    0.000  348.344    0.000 fromnumeric.py:2912(prod)
              107888664  344.826    0.000  344.826    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632947: <Attempt8_DoorsAndKey_option_critic_2> in cluster <dcc> Done

Job <Attempt8_DoorsAndKey_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:36:19 2021
Job was executed on host(s) <n-62-23-20>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:52 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 16 23:16:52 2021
Terminated at Wed May 19 23:12:23 2021
Results reported at Wed May 19 23:12:23 2021

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

    CPU time :                                   258790.25 sec.
    Max Memory :                                 790 MB
    Average Memory :                             778.34 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15594.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258978 sec.
    Turnaround time :                            632164 sec.

The output (if any) is above this job summary.


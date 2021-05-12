
# Parameters

    Name :                      Attempt5_SuperLevel2_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel2
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      35869719880 function calls (34794994804 primitive calls) in 258901.84 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.840 258901.840 {built-in method builtins.exec}
                      1    0.329    0.329 258901.839 258901.839 <string>:1(<module>)
                      1 3884.770 3884.770 258901.510 258901.510 optionCritic.py:195(option_critic_run)
                1204848    9.909    0.000 127482.544    0.106 tensor.py:195(backward)
                1204848   13.165    0.000 127472.442    0.106 __init__.py:68(backward)
                1204848 127430.157    0.106 127430.157    0.106 {method 'run_backward' of 'torch._C._EngineBase' objects}
               38555136 6502.808    0.000 80113.904    0.002 optionCritic.py:143(actor_loss_fn)
        1422165324/351356655 7310.010    0.000 79411.126    0.000 module.py:866(_call_impl)
              118978741  619.454    0.000 74023.297    0.001 optionCritic.py:70(get_state)
              118978741 1608.963    0.000 71592.327    0.001 container.py:117(forward)
              237957482  684.889    0.000 45612.501    0.000 conv.py:398(forward)
              237957482  354.235    0.000 44656.811    0.000 conv.py:390(_conv_forward)
              237957482 44302.576    0.000 44302.576    0.000 {built-in method conv2d}
               38555136 2491.042    0.000 14926.524    0.000 optionCritic.py:91(get_action)
              470335396 1177.969    0.000 14623.364    0.000 linear.py:93(forward)
              470335396  459.629    0.000 12961.402    0.000 functional.py:1737(linear)
              470335396 12385.279    0.000 12385.279    0.000 {built-in method torch._C._nn.linear}
               38555136  820.110    0.000 9680.525    0.000 optionCritic.py:80(predict_option_termination)
                1204848   28.006    0.000 6879.077    0.006 optimizer.py:84(wrapper)
                1204848   15.932    0.000 6771.799    0.006 grad_mode.py:24(decorate_context)
                1204848   81.283    0.000 6728.466    0.006 adam.py:55(step)
                1204848  454.081    0.000 6555.644    0.005 _functional.py:53(adam)
               77110272  851.378    0.000 5614.789    0.000 distribution.py:34(__init__)
              356936223  346.699    0.000 5070.549    0.000 activation.py:713(forward)
               38555136  427.094    0.000 4993.864    0.000 categorical.py:115(log_prob)
              356936223  386.464    0.000 4723.849    0.000 functional.py:1364(leaky_relu)
                1204848    6.937    0.000 4350.981    0.004 game.py:42(step)
                1204848   12.407    0.000 4255.561    0.004 layers.py:827(step)
              356936223 4254.962    0.000 4254.962    0.000 {built-in method torch._C._nn.leaky_relu}
               38555136  556.694    0.000 4175.176    0.000 categorical.py:49(__init__)
              116411294  275.275    0.000 3970.881    0.000 optionCritic.py:77(get_Q)
               38555136  283.630    0.000 3689.208    0.000 bernoulli.py:34(__init__)
                1204848   61.191    0.000 3210.052    0.003 layers.py:17(step)
               38555136  197.110    0.000 3143.110    0.000 layer.py:106(move)
               77411484  283.429    0.000 3109.355    0.000 optionCritic.py:88(get_terminations)
                 301212   49.573    0.000 2990.345    0.010 optionCritic.py:116(critic_loss_fn)
               38555136 1707.699    0.000 2541.384    0.000 constraints.py:398(check)
               38555136  324.644    0.000 2201.952    0.000 layers.py:844(check)
               38555136  359.938    0.000 1997.162    0.000 distribution.py:240(_validate_sample)
              118978741  159.668    0.000 1483.880    0.000 activation.py:101(forward)
               33735732 1466.433    0.000 1466.433    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               38555136 1426.280    0.000 1426.280    0.000 constraints.py:364(check)
               38555136  267.874    0.000 1400.338    0.000 bernoulli.py:86(sample)
               38555136  714.507    0.000 1382.155    0.000 categorical.py:123(entropy)
              118978741  155.628    0.000 1324.212    0.000 functional.py:1195(relu)
             1845209380 1304.491    0.000 1304.589    0.000 module.py:934(__getattr__)
               38555136 1277.551    0.000 1277.551    0.000 constraints.py:249(check)
              115665408  171.024    0.000 1261.689    0.000 utils.py:106(__get__)
               16867866 1241.591    0.000 1241.591    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              269885952 1197.319    0.000 1197.319    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              118978741  123.586    0.000 1150.382    0.000 flatten.py:39(forward)
              118978741 1146.708    0.000 1146.708    0.000 {built-in method relu}
              116267832  126.157    0.000 1088.941    0.000 tensor.py:525(__rsub__)
               16867866 1073.766    0.000 1073.766    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               77110272  363.350    0.000 1039.626    0.000 functional.py:46(broadcast_tensors)
                1204849  121.056    0.000 1027.299    0.001 layers.py:793(update)
              118978741 1026.796    0.000 1026.796    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               38555136  267.055    0.000  981.663    0.000 categorical.py:108(sample)
               38555136   50.271    0.000  956.824    0.000 categorical.py:88(logits)
              116267832  941.127    0.000  941.127    0.000 {built-in method rsub}
               13253328   33.439    0.000  906.764    0.000 tensor.py:575(__iter__)
               38555136   52.463    0.000  906.553    0.000 utils.py:82(probs_to_logits)
             1435418652  899.734    0.000  899.734    0.000 {built-in method torch._C._get_tracing_state}
              115966620  886.943    0.000  886.943    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              115665408  867.203    0.000  867.203    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               77411484  865.852    0.000  865.852    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             6321676459  854.806    0.000  864.000    0.000 {built-in method builtins.len}
               13253328  852.687    0.000  852.687    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               38555136  163.591    0.000  820.626    0.000 utils.py:11(broadcast_all)
               33735732  784.099    0.000  784.099    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               16867866  774.608    0.000  774.608    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               16867866  754.306    0.000  754.306    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             5807640037  732.875    0.000  732.875    0.000 {method 'values' of 'collections.OrderedDict' objects}
              115665408  705.195    0.000  705.195    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               38555136  649.029    0.000  649.029    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 301212  511.209    0.002  642.966    0.002 replaybuffer.py:42(sample_option_critic)
               38555136  127.494    0.000  617.477    0.000 layers.py:838(isFree)
               77110272  564.893    0.000  564.893    0.000 {built-in method broadcast_tensors}
               38555136  108.523    0.000  542.126    0.000 utils.py:77(clamp_probs)
                1204848   59.642    0.000  513.194    0.000 replaybuffer.py:34(save_option_critic)
              346297407  395.038    0.000  489.983    0.000 layer.py:103(isFree)
               38555136  352.226    0.000  483.136    0.000 layers.py:471(check)
              116569044  468.269    0.000  468.269    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               13253339  271.096    0.000  458.636    0.000 layer.py:159(update)
               38555136  436.129    0.000  436.129    0.000 {built-in method bernoulli}
               38555136  433.603    0.000  433.603    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               38555136  427.918    0.000  427.918    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               38698598  426.033    0.000  426.033    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             1024478378  265.943    0.000  381.207    0.000 enum.py:646(__hash__)
              231933240  368.583    0.000  368.583    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               77110272  364.784    0.000  364.784    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1204848   60.726    0.000  363.460    0.000 optimizer.py:189(zero_grad)
               38555136  355.326    0.000  355.326    0.000 {built-in method clamp}
               38555136  189.784    0.000  320.721    0.000 layers.py:246(check)
               38555136  311.964    0.000  311.964    0.000 {built-in method log}
               38555136  306.510    0.000  306.510    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               38555136  207.164    0.000  295.257    0.000 layers.py:77(check)
               38555136  281.567    0.000  281.567    0.000 {built-in method all}
                8132728  281.012    0.000  281.012    0.000 {built-in method tensor}
               38555136  150.777    0.000  280.914    0.000 layers.py:286(check)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618612: <Attempt5_SuperLevel2_option_critic_2> in cluster <dcc> Done

Job <Attempt5_SuperLevel2_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:27 2021
Job was executed on host(s) <n-62-31-4>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sat May  8 23:13:45 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 23:13:45 2021
Terminated at Tue May 11 23:09:02 2021
Results reported at Tue May 11 23:09:02 2021

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

    CPU time :                                   258281.34 sec.
    Max Memory :                                 1157 MB
    Average Memory :                             1142.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15227.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258972 sec.
    Turnaround time :                            507455 sec.

The output (if any) is above this job summary.


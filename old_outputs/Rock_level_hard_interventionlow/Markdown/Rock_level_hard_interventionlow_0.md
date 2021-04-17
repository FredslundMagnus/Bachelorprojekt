
# Parameters

    Name :                      Rock_level_hard_interventionlow-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     11.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.1
    Replay size :               50000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      41311346857 function calls (41167419242 primitive calls) in 39311.62 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39311.617 39311.617 {built-in method builtins.exec}
                      1    0.900    0.900 39311.617 39311.617 <string>:1(<module>)
                      1  103.813  103.813 39310.717 39310.717 main.py:13(teleport)
                2570218    9.005    0.000 17110.811    0.007 game.py:27(step)
                2570218   12.224    0.000 16566.984    0.006 layers.py:373(step)
                2570218  204.326    0.000 11263.788    0.004 layers.py:18(step)
              257021800  526.933    0.000 11037.317    0.000 layer.py:74(move)
                5140436   17.335    0.000 10850.538    0.002 agent.py:26(learn)
                5140436  290.456    0.000 9138.013    0.002 learner.py:42(Qlearn)
              257021800  769.543    0.000 8547.839    0.000 layers.py:390(check)
                2570218   81.137    0.000 6481.205    0.003 agent.py:50(_learn)
                2570219  261.190    0.000 5275.757    0.002 layers.py:344(update)
              257021800 4332.724    0.000 4928.252    0.000 layers.py:76(check)
        161917663/17991059  596.251    0.000 4862.195    0.000 module.py:866(_call_impl)
               12850623   43.488    0.000 4513.584    0.000 network.py:24(forward)
               12850623  142.648    0.000 4394.680    0.000 container.py:117(forward)
                2570218   72.046    0.000 4342.524    0.002 agent.py:101(_learn)
                5140436   41.003    0.000 3535.717    0.001 optimizer.py:84(wrapper)
                2570218 1986.679    0.001 3420.360    0.001 replaybuffer.py:27(teleporter_save_data)
                5140436   21.071    0.000 3355.087    0.001 grad_mode.py:24(decorate_context)
                5140436  133.909    0.000 3288.095    0.001 adam.py:55(step)
                5139969  106.861    0.000 3008.034    0.001 agent.py:45(__call__)
                5140436  684.653    0.000 2992.218    0.001 _functional.py:53(adam)
                2570218 1435.295    0.001 2923.925    0.001 agent.py:77(interveen)
                5140436   19.116    0.000 2344.448    0.000 tensor.py:195(backward)
                5140436   19.665    0.000 2324.597    0.000 __init__.py:68(backward)
                5140436 2210.202    0.000 2210.202    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7950529   68.296    0.000 2200.785    0.000 layers.py:394(restart)
               23131971 1386.315    0.000 2069.566    0.000 layer.py:119(update)
              257021800  369.553    0.000 1730.893    0.000 layers.py:384(isFree)
                2570218  903.707    0.000 1692.896    0.001 replaybuffer.py:23(sample_data)
               25701246   55.343    0.000 1659.945    0.000 conv.py:398(forward)
                2570218  975.129    0.000 1601.164    0.001 agent.py:59(modify)
               25701246   32.774    0.000 1581.051    0.000 conv.py:390(_conv_forward)
               25701246 1548.277    0.000 1548.277    0.000 {built-in method conv2d}
                7950529   32.439    0.000 1397.133    0.000 level.py:8(__init__)
             1914090794 1113.425    0.000 1361.340    0.000 layer.py:71(isFree)
                7950529  194.564    0.000 1249.795    0.000 levels.py:95(generate)
               33411433   65.701    0.000 1211.007    0.000 linear.py:93(forward)
              142842770 1197.423    0.000 1197.423    0.000 {built-in method clone}
               33411433   26.067    0.000 1116.155    0.000 functional.py:1737(linear)
               33411433 1084.001    0.000 1084.001    0.000 {built-in method torch._C._nn.linear}
             4377485867  727.981    0.000 1045.049    0.000 enum.py:646(__hash__)
                7710187   42.471    0.000  936.283    0.000 agent.py:54(modify_board)
                2570218   31.477    0.000  935.056    0.000 agent.py:96(__call__)
               10628370  780.310    0.000  780.310    0.000 {built-in method tensor}
               23131495  761.330    0.000  761.330    0.000 {built-in method cat}
               71554761   98.061    0.000  713.740    0.000 layer.py:48(restart)
               15901058   91.284    0.000  687.346    0.000 level.py:41(notUsed)
              257021800  411.733    0.000  665.354    0.000 layers.py:216(check)
              257021800  394.966    0.000  655.198    0.000 layers.py:230(check)
               46262056   34.848    0.000  651.299    0.000 activation.py:713(forward)
                5140436    5.110    0.000  649.196    0.000 game.py:23(board)
              257021900   71.758    0.000  646.630    0.000 {built-in method builtins.all}
              257021800  385.694    0.000  625.784    0.000 layers.py:244(check)
                7710187  622.475    0.000  622.475    0.000 {built-in method torch._C._nn.one_hot}
                2570218   41.244    0.000  616.501    0.000 replaybuffer.py:19(stacker)
               46262056   38.816    0.000  616.451    0.000 functional.py:1364(leaky_relu)
              790371966  184.048    0.000  603.764    0.000 layers.py:350(<genexpr>)
               92527848  571.203    0.000  571.203    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               46262056  570.073    0.000  570.073    0.000 {built-in method torch._C._nn.leaky_relu}
             5964335273  555.034    0.000  555.034    0.000 layer.py:67(positions)
                5140436   95.286    0.000  530.900    0.000 optimizer.py:189(zero_grad)
               92527848  522.631    0.000  522.631    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              257021800  346.838    0.000  513.312    0.000 layers.py:63(check)
             1005666095  353.471    0.000  476.461    0.000 layer.py:98(add)
             2053290106  457.842    0.000  457.842    0.000 layer.py:114(elements)
               10520747  148.686    0.000  417.088    0.000 random.py:315(sample)
              257021900  263.455    0.000  396.485    0.000 layers.py:110(isDone)
                7950629  191.062    0.000  389.816    0.000 layers.py:33(reset)
              424027338  186.646    0.000  388.196    0.000 layer.py:94(remove)
              397526450  363.800    0.000  363.800    0.000 level.py:32(inverse)
                2570218  208.015    0.000  354.223    0.000 collector.py:54(collect)
               46263924  344.126    0.000  344.126    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              257021800  217.342    0.000  328.768    0.000 layers.py:203(check)
             4377504770  317.072    0.000  317.072    0.000 {built-in method builtins.hash}
                5139969  112.476    0.000  302.008    0.000 exploration.py:53(softmaxer)
               46263924  301.518    0.000  301.518    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              150552957  292.878    0.000  292.878    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               46263924  278.617    0.000  278.617    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               46263924  278.251    0.000  278.251    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              323847522  203.006    0.000  252.514    0.000 tensor.py:906(grad)
        2701062991/2701062989  179.025    0.000  213.000    0.000 {built-in method builtins.len}
              367090748  144.537    0.000  207.274    0.000 random.py:250(_randbelow_with_getrandbits)
               46263924  206.959    0.000  206.959    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5140436    7.169    0.000  205.504    0.000 loss.py:527(forward)
             3061449512  202.288    0.000  202.288    0.000 {method 'append' of 'list' objects}
              257021800   89.371    0.000  199.776    0.000 layers.py:99(<listcomp>)
                5140436   18.295    0.000  198.335    0.000 functional.py:2898(mse_loss)
             1914090794  178.442    0.000  178.442    0.000 layer.py:175(isBlocking)
               15901058   12.631    0.000  177.713    0.000 level.py:38(elementsIn)
              424027338  168.491    0.000  168.491    0.000 {method 'remove' of 'list' objects}
               15421308  153.023    0.000  153.023    0.000 {built-in method sum}
                5140436  121.817    0.000  121.817    0.000 {built-in method torch._C._nn.mse_loss}
               25701246   17.712    0.000  112.588    0.000 flatten.py:39(forward)
                5141206  110.329    0.000  110.329    0.000 {built-in method max}
                7710654   12.264    0.000  107.285    0.000 tensor.py:525(__rsub__)
               15901058   50.677    0.000   99.918    0.000 level.py:39(<listcomp>)
                5139969   95.153    0.000   95.153    0.000 {built-in method multinomial}
               25701246   94.876    0.000   94.876    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9444632: <Rock_level_hard_interventionlow_0> in cluster <dcc> Done

Job <Rock_level_hard_interventionlow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:59 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 13:04:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 13:04:27 2021
Terminated at Sun Mar 21 23:59:46 2021
Results reported at Sun Mar 21 23:59:46 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   39209.92 sec.
    Max Memory :                                 5849 MB
    Average Memory :                             4260.09 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2343.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39319 sec.
    Turnaround time :                            78647 sec.

The output (if any) is above this job summary.

